# Copyright 2022 Cognite AS
from .correlation import pearson_correlation
from .outliers import remove_outliers


TOOLBOX_NAME = "Statistics"

__all__ = ["remove_outliers, pearson_correlation"]
