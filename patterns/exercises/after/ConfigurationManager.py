class ConfigurationManager:
    """
    Gestiona la configuración global de la aplicación.
    """

    _instance = None

    def __init__(self):
        # El constructor no debería ser llamado directamente.
        raise RuntimeError("¡Llamar a get_instance() en su lugar!")

    @classmethod
    def get_instance(cls):
        """Obtiene la única instancia de la clase."""
        if cls._instance is None:
            # Crea la instancia si no existe.
            cls._instance = cls.__new__(cls)
            cls._instance.admin_name = "admin@sistema.com"
        return cls._instance

    def get_admin_name(self):
        return self.admin_name