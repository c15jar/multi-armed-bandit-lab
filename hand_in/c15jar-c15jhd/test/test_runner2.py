import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.dirname(parent_dir))

import bandit

def simulate():
    results = []
    sim = bandit.simulator.Simulator()
    
    for _ in range(0, 20):
        bandit.ref_bandit.sums = [0] * len(bandit.arms)
        sim.randomize()
        bandit_reward = sim.simulate(bandit.bandit)
        print("Bandit Reward: " + str(bandit_reward))
        ref_bandit_reward = sim.simulate(bandit.ref_bandit)
        print("REF Bandit Reward: " + str(ref_bandit_reward))
        ref_plus_bonus = ref_bandit_reward * 1.05
        result = 0
        if (bandit_reward > ref_plus_bonus):
            result = 1
        results.append(result)
    return results

def test_performance():
    s = sum(simulate())
    print(s)
    assert s > 17
    


test_performance()
