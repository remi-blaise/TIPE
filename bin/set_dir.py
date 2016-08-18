"""Set parent directory as root directory"""
import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
os.chdir(parent_dir) 			# Set main dir for resources
sys.path.append(parent_dir)		# Set main dir for import paths
