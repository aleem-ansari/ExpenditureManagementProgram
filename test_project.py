from project import all_expenses, counter, display_menu, view_expense, remove_expense, edit_expense, add_expense
from unittest.mock import patch



def test_display_menu():
    expected_output = """┍━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━┑
│  S.No.  │ Option            │  Command  │
┝━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━┥
│    1    │ Add an Expense    │     A     │
├─────────┼───────────────────┼───────────┤
│    2    │ Edit an Expense   │     E     │
├─────────┼───────────────────┼───────────┤
│    3    │ Remove an Expense │     R     │
├─────────┼───────────────────┼───────────┤
│    4    │ View all Expenses │     V     │
├─────────┼───────────────────┼───────────┤
│    5    │ Exit the Program  │     X     │
┕━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━┙"""  # Fill this with the exact string you expect from display_menu()
    assert display_menu() == expected_output



def test_view_expense():
    counter = 0
    assert view_expense() == "\nNo entries to view.\n"



def test_remove_expense():
    assert remove_expense() == "\nNo entries to remove.\n"



def test_edit_expenses():
    assert edit_expense() == "\nNo entries to edit.\n"



@patch('builtins.input', side_effect=['Test Expense', '100'])
def test_add_expense(mock_input):
    global counter
    counter = 0
    global all_expenses
    all_expenses = []
    assert add_expense() == "\nExpense added\n"
    assert all_expenses == []