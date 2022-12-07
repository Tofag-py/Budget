
function calculateBudget() {
  // get user input
  var monthlyIncome = document.getElementById("monthlyIncome").value;
  var monthlyExpenses = document.getElementById("monthlyExpenses").value;
  var budgetResult;
  
  // validate user input
  if (isNaN(monthlyIncome) || monthlyIncome < 0 || isNaN(monthlyExpenses) || monthlyExpenses < 0) {
    alert("Please enter valid numbers for your monthly income and expenses.");
    return;
  }
  
  // calculate the budget result
  budgetResult = monthlyIncome - monthlyExpenses;
  
  // display the result in an easy-to-read format
  if (budgetResult > 0) {
    alert("Your budget is in surplus by $" + budgetResult + ".");
  } else if (budgetResult < 0) {
    alert("Your budget is in deficit by $" + Math.abs(budgetResult) + ".");
  } else {
    alert("Your budget is balanced.")
  }
}