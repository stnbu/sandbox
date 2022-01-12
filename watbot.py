"""Try to model "intelligent agents"

To be general we have a problem with trying to model every thing you could do
and whether it might affect one in 7.5 billion people. But you say "let's make
simlifying assumptions so we don't have to update ALL people."

Or you might wonder before that point: Why try to model with the idea that you
_can potentially_ update any human anywhere at any time.

I can drunkenly call my aunt and really complicate her feelings for me.

Et cetera.

And there's also facebook. If you're modeling "generally" (assuming that's even
a good goal), you have to at least potentially update every member of the network,
given what kind of output "you" have, how you intend to emit it.

But that seems like an immediate barrier to scaling. If you _potentially_ need
to update every member, you'll need to examine your "output" and somehow decide
"what is the smallest set of members you can get away with updating?"

A possible interesing observation: this data is embedded entirely within the
"output". Examples:

* I can make an anonymous room service request to a hotel in Russia, causing all kinds of chaos: internet
* I can experiment with chemicals and learn how to make loud bangs. Using this as a means of "emitting data"
  and "updating others", I'm limited to the people within a few kilometers.
* If I fail to shower for a few days I can only "update" people near me on the bus.

Notice that all of the above stem from me, but embedded in "data/medium tuple"

In the above examples: room-service/internet, bang/atmosphere, stank/stank

We may or may not be able to generalize or model the above, but the bigger point is that "the nature of the medium" (er, physics)
and the "quality of the data" together suggest approaches for narrowing down the members to update.

So the trick is, understand the `get_magical_gamma` function below.
"""

class Output:

    def __init__(self):
        
        pass

def get_magical_gamma(output):
    """Here we try to stop the madness. This obviously can't scale if every call for any agent to emit data requires updating every single one.
    """

class Agent:

    def emit(self, output):
        gamma = get_magical_gamma(output)
        network = get_all_agents(gamma)
        for other in network:
            other.percieve(output)

    def add_sense(self):
        self.senses.add(Sense(self, callback))
        

class Sense:

    def __init__(self, agent, callback):
        self.agent = agent
        self.callback = callback

    def on_callback(self, identity, input):
        self.agent.memory.update(identity, input)

def f():
    pass

if __name__ == '__main__':
    f()
