from gui import run_gui

def get_inputs():
  Principle = float(input("What is your Principle amount?: "))
  rate = float(input("What is your annual interest rate (in percent)?: ")) / 100
  time = int(input("How long (in years) do you want it to compound?: "))
  num_compounds = 12  # Assuming compounds monthly
  return Principle, rate, time, num_compounds


def compound_interest(Principal, rate, time, num_compounds):
  amount = Principal * (1 + rate / num_compounds) ** (num_compounds * time)
  return amount


def main():
  print("Welcome to your compound interest calculator!\n")

  # Get user inputs
  Principle, rate, time, num_compounds = get_inputs()

  # Calculate compound interest
  amount = compound_interest(Principle, rate, time, num_compounds)

  # Print the result
  print(f'After compounding for {time} years at {rate*100:.2f}% interest annually, '
        f'your principle of ${Principle} will total ${amount:,.2f}')


if __name__ == "__main__":
  main()
