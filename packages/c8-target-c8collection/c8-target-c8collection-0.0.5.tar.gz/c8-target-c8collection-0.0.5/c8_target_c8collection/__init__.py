"""GDN data connector target for C8 collections."""
from c8connector import C8Connector


class C8CollectionTargetConnector(C8Connector):
    """C8CollectionTargetConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "c8collection"

    def type(self) -> str:
        """Returns the type of the connector."""
        return "target"

    def version(self) -> str:
        """Returns the version of the connector."""
        return "0.0.1"

    def description(self) -> str:
        """Returns the description of the connector."""
        return "GDN data connector target for C8 Collections"

    def validate(self, integration: dict) -> bool:
        """Validate given configurations against the connector."""
        return True

    def samples(self, integration: dict) -> list:
        """Fetch sample data using the provided configurations."""
        return []

    def config(self) -> dict:
        """Get configuration parameters for the connector."""
        return {
            "email": "mandatory",
            "password": "mandatory",
            "region": "mandatory",
            "fabric": "mandatory",
            "tenant": "mandatory",
            "target_collection": "mandatory",
            "schemas": "mandatory"
        }
