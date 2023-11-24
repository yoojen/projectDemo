from api.bm.views import bm_views
from models.engine import *
from flask import jsonify, request
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


@bm_views.route('/expenses', methods=['GET', 'POST'], strict_slashes=False)
def expenses():
    """returns all objects from db"""
    data = []
    if (request.method == 'POST'):
        print("yes")
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        type = request.form['type']
        desc = request.form['desc']
        data.append(name)
        data.append(desc)
        data.append(int(amount))
        data.append(1)
        data.append(int(category))
        if type == "expenses":
            Expense(data[0], data[1], data[2], data[3], data[4]).save()
            return jsonify(message="data recorded successfully")
        else:
            return jsonify(message="failed")
    else:
        return jsonify(get_object(Expense))


@bm_views.route('/expenses/<string:name>',  strict_slashes=False)
def expense_byName(name):
    """return expense based on ID"""
    data = get_object(Expense)
    for exp in data:
        dbName = exp.get('name').lower()
        if name in dbName:
            return jsonify([exp])
    return jsonify(error="not found")


@bm_views.route('/expenses/<int:expense_id>',  strict_slashes=False)
def expense_byId(expense_id):
    """return expense based on ID"""
    return jsonify(get_objectByID(Expense, expense_id))


@bm_views.route('/expenses/total', strict_slashes=False)
def total_expense():
    """returns total amount spent"""
    sum = 0
    expense_list = get_total(Expense, "expense")
    for exp in expense_list:
        for values in exp.values():
            sum = sum + int(values)
    return jsonify(expense_list, {"total expenses": sum})


@bm_views.route('/expenses/categories', strict_slashes=False)
def expenses_categories():
    """returns category that is spent"""
    res = categoriesOfExpenses(Expense, "expense")
    return jsonify(res)


@bm_views.route('/expenses/category/<int:category_id>', strict_slashes=False)
def expenseMatchingCategoryId(category_id):
    """returns expense which match the category id"""
    Obj = getObjMatchingCategoryId(Expense, category_id)
    return jsonify(Obj)


@bm_views.route('/expenses/<int:expense_id>/category', strict_slashes=False)
def exp_category(expense_id):
    """return category of a certain expense"""
    expense = find_exp_category(Expense, expense_id)
    if expense:
        return jsonify({str(expense.name): [{"category": expense.spend.type}]})
    return jsonify({"null": "yes"})


@bm_views.route('/expenses/amt_gt/<int:amount>', strict_slashes=False)
def get_exp_amt_gt(amount):
    """return expenses which amount is greater than inputs"""
    all_items = amount_gt(Expense, amount, "expense")
    return jsonify(all_items)


@bm_views.route('/expenses/amt_lt/<int:amount>', strict_slashes=False)
def get_exp_amt_lt(amount):
    """return expenses where amount is less than input"""
    all_items = amount_lt(Expense, amount, "expense")
    return jsonify(all_items)


@bm_views.route('/expenses/date/<string:date_range_1>/<string:date_range_2>', strict_slashes=False)
def filter_by_date(date_range_1, date_range_2):
    """returns expenses in a certain date range"""
    data = filter_obj_byDate(Expense, date_range_1, date_range_2)
    if (data):
        return jsonify(data)
    return []
