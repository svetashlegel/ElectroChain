def clear_debts(queriset):
    """An action that allows you to clear debt from selected objects"""

    queriset.update(debt=0)


clear_debts.short_description = "Очистить задолженности у выбранных объектов"
