from typing import Iterable, Union

import numpy as np
from scipy.linalg import block_diag
from sklearn.utils.validation import check_is_fitted

from cca_zoo.models import MCCA
from cca_zoo.utils import _check_views


class PartialCCA(MCCA):
    r"""
    A class used to fit a partial cca model. The key difference between this and a vanilla CCA or MCCA is that
    the canonical score vectors must be orthogonal to the supplied confounding variables.

    References
    ----------
    Rao, B. Raja. "Partial canonical correlations." Trabajos de estadistica y de investigación operativa 20.2-3 (1969): 211-219.

    Example
    -------
    >>> from cca_zoo.models import PartialCCA
    >>> X1 = np.random.rand(10,5)
    >>> X2 = np.random.rand(10,5)
    >>> partials = np.random.rand(10,3)
    >>> model = PartialCCA()
    >>> model.fit((X1,X2),partials=partials).score((X1,X2))
    array([0.99993046])

    """

    def __init__(
            self,
            latent_dims: int = 1,
            scale: bool = True,
            centre=True,
            copy_data=True,
            random_state=None,
            c: Union[Iterable[float], float] = None,
            eps=1e-3,
    ):
        super().__init__(
            latent_dims=latent_dims,
            scale=scale,
            centre=centre,
            copy_data=copy_data,
            random_state=random_state,
        )
        self.c = c
        self.eps = eps

    def fit(self, views: Iterable[np.ndarray], y=None, partials=None, **kwargs):
        super(MCCA, self).fit(views, y=y, partials=partials, **kwargs)

    def _setup_evp(self, views: Iterable[np.ndarray], partials=None, **kwargs):
        if partials is None:
            raise ValueError(
                f"partials is {partials}. Require matching partials to transform with"
                f"partial CCA."
            )
        self.confound_betas = [np.linalg.pinv(partials) @ view for view in views]
        views = [
            view - partials @ np.linalg.pinv(partials) @ view
            for view, confound_beta in zip(views, self.confound_betas)
        ]
        all_views = np.concatenate(views, axis=1)
        C = all_views.T @ all_views / self.n
        # Can regularise by adding to diagonal
        D = block_diag(
            *[
                (1 - self.c[i]) * m.T @ m / self.n + self.c[i] * np.eye(m.shape[1])
                for i, m in enumerate(views)
            ]
        )
        C -= block_diag(*[view.T @ view / self.n for view in views]) - D
        D_smallest_eig = min(0, np.linalg.eigvalsh(D).min()) - self.eps
        D = D - D_smallest_eig * np.eye(D.shape[0])
        self.splits = np.cumsum([0] + [view.shape[1] for view in views])
        return views, C, D

    # TODO TRANSFORM
    def transform(self, views: Iterable[np.ndarray], partials=None, **kwargs):
        if partials is None:
            raise ValueError(
                f"partials is {partials}. Require matching partials to transform with"
                f"partial CCA."
            )
        check_is_fitted(self, attributes=["weights"])
        views = _check_views(
            *views, copy=self.copy_data, accept_sparse=self.accept_sparse
        )
        views = self._centre_scale_transform(views)
        transformed_views = []
        for i, (view) in enumerate(views):
            transformed_view = (
                                       view - partials @ self.confound_betas[i]
                               ) @ self.weights[i]
            transformed_views.append(transformed_view)
        return transformed_views
