"""Set parent directory as root directory"""
import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
main_dir = os.path.dirname(parent_dir)
os.chdir(main_dir) 			# Set main dir for resources
sys.path.append(main_dir)	# Set main dir for import paths
