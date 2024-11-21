import logging
import sys
import os

_loggers: dict[str, logging.Logger] = {}

def get_module_logger(module_name: str = "__main__") -> logging.Logger:
    """
    モジュール用のロガーを取得または作成します。
    
    Args:
        module_name: モジュール名（通常は__name__を使用）
    
    Returns:
        設定済みのロガーインスタンス
    """
    if module_name in _loggers:
        return _loggers[module_name]
    
    logger = logging.getLogger(module_name)
    
    if not logger.handlers:
        level = logging.INFO if os.getenv('DEBUG_MODE', '').lower() == 'true' else logging.WARNING
        logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    _loggers[module_name] = logger
    return logger