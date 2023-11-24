from api.bm.views import bm_views
from models.engine import *
from flask import jsonify, request
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


@bm_views.route('/plans', methods=['GET', 'POST'], strict_slashes=False)
def planings():
    """returns all objects from db"""
    data = []
    print(request.method)
    if (request.method == 'POST'):
        print(request.form)
        name = request.form.get('name')
        amount = request.form.get('amount')
        desc = request.form.get('desc')
        category = request.form.get('category')
        print(name, amount, category, desc)
        Plan(amount, name,  desc, category, 1).save()
        return jsonify(message="data recorded successfully")
    else:
        return jsonify(get_object(Plan))


# @bm_views.route('/expenses/<string:name>',  strict_slashes=False)
# def expense_byName(name):
#     """return expense based on ID"""
#     data = get_object(Expense)
#     for exp in data:
#         dbName = exp.get('name').lower()
#         if name in dbName:
#             return jsonify([exp])
#     return jsonify(error="not found")


# @bm_views.route('/expenses/<int:expense_id>',  strict_slashes=False)
# def expense_byId(expense_id):
#     """return expense based on ID"""
#     return jsonify(get_objectByID(Expense, expense_id))


# @bm_views.route('/expenses/total')
# def total_expense():
#     """returns total amount spent"""
#     sum = 0
#     expense_list = get_total(Expense, "expense")
#     for exp in expense_list:
#         for values in exp.values():
#             sum = sum + int(values)
#     return jsonify(expense_list, {"total expenses": sum})


# @bm_views.route('/expenses/categories')
# def expenses_categories():
#     """returns category that is spent"""
#     res = categoriesOfExpenses(Expense, "expense")
#     return jsonify(res)


# @bm_views.route('/expenses/<int:expense_id>/category')
# def exp_category(expense_id):
#     expense = find_exp_category(Expense, expense_id)
#     if expense:
#         return jsonify({str(expense.name): [{"category": expense.spend.type}]})
#     return jsonify({"null": "yes"})


# @bm_views.route('/expenses/amt_gt/<int:amount>')
# def get_exp_amt_gt(amount):
#     all_items = amount_gt(Expense, amount, "expense")
#     return jsonify(all_items)


# @bm_views.route('/expenses/amt_lt/<int:amount>')
# def get_exp_amt_lt(amount):
#     all_items = amount_lt(Expense, amount, "expense")
#     return jsonify(all_items)


# @bm_views.route('/expenses/date/<string:date_range_1>/<string:date_range_2>')
# def filter_by_date(date_range_1, date_range_2):
#     data = filter_obj_byDate(Expense, date_range_1, date_range_2)
#     if (data):
#         return jsonify(data)
#     return []
