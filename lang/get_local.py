import importlib
import sql


# Gets sample for user's language
def get_sample(sample_name: str, name: str):

    sql_language = sql.Language(name)
    language = sql_language.get_language()

    language_samples = importlib.import_module(f"langs.{language.lower()}")
    samples = language_samples.Samples()

    # bruh
    sample = eval(f"samples.{sample_name}")

    return sample


