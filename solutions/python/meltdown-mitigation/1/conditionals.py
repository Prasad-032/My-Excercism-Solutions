def is_criticality_balanced(temperature, neutrons_emitted):
        return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
def reactor_efficiency(voltage, current, theoretical_max_power):
        efficiency = ((voltage * current) / theoretical_max_power) * 100
        if efficiency >= 80:
                return "green"
        if efficiency >= 60 and efficiency < 80:
                return "orange"
        if efficiency >= 30 and efficiency < 60:
                return "red"
        if efficiency < 30:
                return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
        value = temperature * neutrons_produced_per_second
        low_limit = 0.9 * threshold
        high_limit = 1.1 * threshold

        if value < low_limit:
                return "LOW"
        elif low_limit <= value <= high_limit:
                return "NORMAL"
        else:
                return "DANGER"
