Last update: April 6, 2019 18:45

***** This readme file will be used as 'project status' unitl the code is complete and robust *****

# lazor_solver
module to solve for board puzzles of the "Lazors" game in Android and iOS

Missing functions:
  - image loader of board to solve
  - image exporter of solved board


The loader and solver are running smoothly, however there are multiple issues that can be addressed and solved:
  - the function *get_possible_combs_perm* returns more than needed combinations, this can be due to sorting issues
  - possibly after commiting the image loader, merge with the bff_loader to take input as either bff file or image
