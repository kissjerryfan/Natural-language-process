from oscopilot import FridayAgent
from oscopilot import ToolManager
from oscopilot import FridayExecutor, FridayPlanner, FridayRetriever
# from examples.light_friday import LightFriday
from oscopilot.utils import setup_config, setup_pre_run

args = setup_config()
if not args.query:
    # args.query = "Copy any text file located in the working_dir/document directory that contains the word 'agent' to a new folder named 'agents' "
    # args.query = "create a profile.csv file in working_dir and create some fake profile data in it"
    args.query = "please help me order in Xiangjiang"
task = setup_pre_run(args)
agent = FridayAgent(FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args)
# agent = LightFriday(config=args)
agent.run(task=task)
