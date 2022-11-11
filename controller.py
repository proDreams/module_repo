import model
import view


def run():
    model.init(view.get_value(), view.get_value(), view.get_value())
    data = model.calculation()
    view.view_data(data)
