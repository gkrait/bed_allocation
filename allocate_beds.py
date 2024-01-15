def allocate_beds(beds, patients, R1, R2):
  """
  Allocates beds to patients.

  Args:
    beds: The number of beds available.
    patients: The list of patients.
    R1: The revenue per bed booked for patient 1.
    R2: The revenue per bed booked for patient 2.

  Returns:
    The maximum total revenue.
  """

  # Initialize the dynamic programming table.
  dp = [[0 for _ in range(beds + 1)] for _ in range(len(patients) + 1)]

  # Iterate over the patients.
  for i in range(1, len(patients) + 1):
    # Iterate over the number of beds available.
    for j in range(1, beds + 1):
      # If the current patient is a patient 1, then we can only allocate a bed to them if there are enough beds available.
      if patients[i - 1] == 1 and j < i:
        dp[i][j] = dp[i - 1][j]
      # Otherwise, we can either allocate a bed to the current patient or not.
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (R1 if patients[i - 1] == 1 else R2))

  # Return the maximum total revenue.
  return dp[len(patients)][beds]


#example
beds = 5
patients = [1, 2, 1, 2, 1]
R1 = 10
R2 = 5

max_revenue = allocate_beds(beds, patients, R1, R2)

print(max_revenue)
