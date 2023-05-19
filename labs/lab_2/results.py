from labs.lab_2.lab_2_interval_sample import Lab2IntervalSample
from labs.lab_2.probability_estimate import ProbabilityEstimate

if __name__ == "__main__":
    print("ЗАВДАННЯ A")
    interval_sample = Lab2IntervalSample(["Маса пакету, г", "Кількість овець"])
    interval_sample.build_table()
    interval_sample.build_discrete_sample_table()
    print(f"Вибіркове середнє: {interval_sample.mean}")
    print(f"Виправлена вибіркова дисперсія: {interval_sample.variance}")
    print(
        f"Вибіркове середнє квадратичне відхилення: {interval_sample.standard_deviation}"
    )
    print(f"Точність оцінки: {interval_sample.assessment_accuracy}")
    print(f"Надійний інтервал: {interval_sample.confidence_interval}")
    print("\nЗАВДАННЯ Б")
    probability_estimate = ProbabilityEstimate()
    print(f"Відносна частота події: {probability_estimate.relative_frequency}")
    print(f"Інтервал надійності: {probability_estimate.confidence_interval}")
