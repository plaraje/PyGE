from typing import TYPE_CHECKING, Optional

from Objects.Core.RenderContext import RenderContext

if TYPE_CHECKING:
    from Objects.Entities.Entity import Entity

class Behaviour:
    def __init__(self, entity: Optional['Entity'] = None):
        self.entity = entity
        self.enabled = True

    def on_attach(self, entity: 'Entity') -> None:
        """Llamado cuando el behaviour se añade a una entidad"""
        self.entity = entity

    def on_detach(self) -> None:
        """Llamado cuando el behaviour se elimina de una entidad"""
        self.entity = None

    def update(self, delta_time: float) -> None:
        """Actualización por frame"""
        pass

    def fixed_update(self, fixed_delta: float) -> None:
        """Actualización física"""
        pass

    def render(self, render_context: 'RenderContext') -> None:
        """Renderizado opcional"""
        pass
