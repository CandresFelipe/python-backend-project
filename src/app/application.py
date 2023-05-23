from components import Components
from fastapi import FastAPI


class Application(FastAPI):
    @property
    def components(self) -> Components:
        components: Components = self.state.components
        return components

    @components.setter
    def components(self, value: Components) -> None:
        self.state.components = value
