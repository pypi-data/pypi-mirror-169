from scipy.optimize import OptimizeResult
from scipy.optimize.optimize import (_status_message, _line_search_wolfe12,
                                     MemoizeJac, _LineSearchError)
import torch

from .function import ScalarFunction


class TorchMemoizeJac(MemoizeJac):

    def __init__(self, fun_, device, dtype):
        def fun(x):
            x = torch.tensor(x, device=device, dtype=dtype)
            f, g, _, _ = fun_(x)
            return float(f), g.cpu().numpy()

        super().__init__(fun)


def line_search_wolfe12(fun, x, p, g, old_f, old_old_f, **kwargs):
    """
    We will use scipy's line search method for now, since pytorch's line
    search does not support an "extra_condition" argument
    """
    device, dtype = x.device, x.dtype

    fun = TorchMemoizeJac(fun, device, dtype)

    alpha, fc, gc, fval, old_fval, g = \
        _line_search_wolfe12(fun, fun.derivative,
                             x.cpu().numpy(), p.cpu().numpy(), g.cpu().numpy(),
                             float(old_f), float(old_old_f), **kwargs)

    fval = torch.tensor(fval, device=device, dtype=dtype)
    old_fval = torch.tensor(old_fval, device=device, dtype=dtype)
    g = torch.tensor(g, device=device, dtype=dtype)

    return alpha, fc, gc, fval, old_fval, g


@torch.no_grad()
def _minimize_cg(f, x0, callback=None, gtol=1e-5, norm=float('inf'),
                 max_iter=None, disp=False, return_all=False):
    """
    Minimization of scalar function of one or more variables using the
    conjugate gradient algorithm.

    Parameters
    ----------
    disp : bool
        Set to True to print convergence messages.
    max_iter : int
        Maximum number of iterations to perform.
    gtol : float
        Gradient norm must be less than `gtol` before successful
        termination.
    norm : float
        Order of norm (Inf is max, -Inf is min).
    return_all : bool, optional
        Set to True to return a list of the best solution at each of the
        iterations.

    """
    disp = int(disp)
    if max_iter is None:
        max_iter = x0.numel() * 200

    # Construct scalar objective function
    sf = ScalarFunction(f, x_shape=x0.shape)
    f_closure = sf.closure

    x = x0.detach().flatten()
    fval, g, _, _ = f_closure(x)
    old_fval = fval + g.norm() / 2  # Sets the initial step guess to dx ~ 1
    if return_all:
        allvecs = [x]
    p = g.neg()
    grad_norm = g.norm(p=norm)
    # nfev = 0

    for k in range(1, max_iter + 1):
        delta = g.dot(g)

        cached_step = [None]

        def polak_ribiere_powell_step(alpha, g1):
            x1 = x + alpha * p
            if g1 is None:
                g1 = f_closure(x1)[1]
            y = g1 - g
            beta = torch.clamp(y.dot(g1) / delta, min=0)
            p1 = -g1 + p.mul(beta)
            torch.norm(g1, p=norm, out=grad_norm)
            return alpha, x1, p1, g1

        def descent_condition(alpha, x1, f1, g1):
            # Polak-Ribiere+ needs an explicit check of a sufficient
            # descent condition, which is not guaranteed by strong Wolfe.
            if g1 is not None:
                g1 = torch.tensor(g1, dtype=x0.dtype, device=x0.device)
            cached_step[:] = polak_ribiere_powell_step(alpha, g1)
            alpha, x, p, g = cached_step

            # Accept step if it leads to convergence or if sufficient
            # descent condition applies.
            return (grad_norm <= gtol) | (p.dot(g) <= -0.01 * g.dot(g))

        try:
            alpha, ls_nevals, _, fval, old_fval, g1 = \
                     line_search_wolfe12(f_closure, x, p, g, fval, old_fval,
                                         c2=0.4, amin=1e-100, amax=1e100,
                                         extra_condition=descent_condition)
        except _LineSearchError:
            warnflag = 2
            msg = _status_message['pr_loss']
            break

        # Reuse already computed results if possible
        if alpha == cached_step[0]:
            alpha, x, p, g = cached_step
        else:
            alpha, x, p, g = polak_ribiere_powell_step(alpha, g1)

        if return_all:
            allvecs.append(x)
        if callback is not None:
            callback(x)

        # check optimality
        if grad_norm <= gtol:
            warnflag = 0
            msg = _status_message['success']
            break

    else:
        warnflag = 1
        msg = _status_message['maxiter']

    if grad_norm.isnan() or fval.isnan() or x.isnan().any():
        warnflag = 3
        msg = _status_message['nan']

    if disp:
        print("%s%s" % ("Warning: " if warnflag != 0 else "", msg))
        print("         Current function value: %f" % fval)
        print("         Iterations: %d" % k)
        # print("         Function evaluations: %d" % nfev)

    result = OptimizeResult(x=x, fun=fval, jac=g, nit=k,  # nfev=nfev,
                            status=warnflag, success=(warnflag == 0),
                            message=msg)
    if return_all:
        result['allvecs'] = allvecs
    return result