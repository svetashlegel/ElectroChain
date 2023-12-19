def clear_debts(queriset):
    queriset.update(debt=0)


clear_debts.short_description = "Очистить задолженности у выбранных объектов"
