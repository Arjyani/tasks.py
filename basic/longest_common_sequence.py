def lcs(s1, s2) -> str:
  """Compare both the strigs and prints
     the loggest common sequence between
     both the strings.

  >>> lcs(“ABCDGH”, “AEDFHR”) 
  3
  """
  cols = len(s1) + 1
  rows = len(s2) + 1

  t = [[0 for i in range(cols)] for i in range(rows)]

  max_length = 0

  for i in range(1, rows):
      for j in range(1, cols):
          if s2[i-1] == s1[j-1]:
              t[i][j] = 1 + t[i-1][j-1]
          else:
              t[i][j] = max(t[i-1][j], t[i][j-1])

          max_length = max(max_length, t[i][j])

  print(max_length)
  
if __name__ == "__main__":
  
  lcs("AGGTAB", "GXTXAYB")
