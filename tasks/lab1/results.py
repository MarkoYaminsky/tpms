from tasks.lab1.discrete_sample import DiscreteSample
from tasks.lab1.lab_1_interval_sample import Lab1IntervalSample

if __name__ == "__main__":
    sample = DiscreteSample()
    sample.order()
    print("1) Дискретний статистичний ряд (вибірка)")
    sample.build_sample_table()
    print(
        f"2) Розмах вибірки: {sample.range}, медіана вибірки: {sample.median}, моди вибірки: {sample.mode}"
    )
    sample.draw_frequency_graph()
    interval_sample = Lab1IntervalSample(sample)
    print("4) Інтервальний статистичний ряд")
    interval_sample.build_table()
    interval_sample.draw_frequency_histogram()
    print(
        f"Мода інтервального статистичного ряду: {interval_sample.mode}, медіана: {interval_sample.median}"
    )
    interval_sample.draw_empirical_distribution_function()
    print(
        f"7) Середнє значення вибірки: {sample.mean}, інтервального статистичного ряду: {interval_sample.mean}"
    )
    print(
        f"8) Дисперсія інтервального статистичного ряду: {interval_sample.variance}, "
        f"середьоквадратичне відхилення: {interval_sample.standard_deviation}"
    )
    print(f"9) Коефіцієнт варіації: {interval_sample.variation_coefficient}")
    print(
        f"10) Центральний емпіричний момент 3 порядку: {interval_sample.get_central_empirical_moment(3)}, "
        f"4 порядку: {interval_sample.get_central_empirical_moment(4)}"
    )
    print(
        f"11) Асиметрія: {interval_sample.skewness}, ексцес: {interval_sample.kurtosis}"
    )
