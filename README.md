Altinferencer
===============
Library to put AltScore models into production


🔩 Installation
===============

* Install using:  pip install git+https://github.com/AltScore/altinference.git

✒️ How to Use
===============

To create the ``Inferer`` object you have to provide:
* The model file path.
* The pipeline file path.
```python
inferer = Inferer("model_path", "pipeline_path")
```

The ``predict_probability`` method receives a dataframe and returns a predicted probability of default.

```python
pd = inferer.predict_probability(data)
```