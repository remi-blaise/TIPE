from lib.inject_arguments import injectArguments

from bridge.events.game_events import *
from bridge.events.action_events import *


class IA:
    """An temp IA for early stage of dev"""
    
    @injectArguments
    def __init__(self, event_dispatcher, neuron_set=set()):
        self.build()
    
    def build(self):
        self.neuron_set.add( Neuron('game.block', { 'x':40, 'y':40 }, Right, 1, self.event_dispatcher) )
        self.neuron_set.add( Neuron('game.block', { 'x':80, 'y': 0 }, Jump, 30, self.event_dispatcher) )
        self.neuron_set.add( Neuron('game.enemy', { 'x':80, 'y': 0 }, Jump, 30, self.event_dispatcher) )


class Neuron:
    """A link between an game event and an action event"""
    
    @injectArguments
    def __init__(self, event_name, coor, action_class, duration, event_dispatcher):
        self.event_dispatcher = event_dispatcher
    
    def event_dispatcher():
        doc = "The event_dispatcher property."
        
        def fget(self):
            return self._event_dispatcher
        
        def fset(self, event_dispatcher):
            """Register the neuron to the event_dispatcher"""
            if hasattr(self, 'listener_id'):
                del self.event_dispatcher
            
            self._event_dispatcher = event_dispatcher
            self.listener_id = self._event_dispatcher.listen(self.event_name, self.onEvent)
            
        def fdel(self):
            """Detach the listener"""
            if hasattr(self, 'listener_id'):
                self._event_dispatcher.detach(self.listener_id)
                del self.listener_id
            
            del self._event_dispatcher
        return locals()
    event_dispatcher = property(**event_dispatcher())
    
    def __del__(self):
        if hasattr(self, 'event_dispatcher'):
            del self.event_dispatcher
    
    
    def onEvent(self, event):
        if self.coor['x'] >= event.left and self.coor['x'] <= event.right \
                and self.coor['y'] >= event.top and self.coor['y'] <= event.bottom:
            self.event_dispatcher.dispatch('action', self.action_class(30, event.current_frame))
