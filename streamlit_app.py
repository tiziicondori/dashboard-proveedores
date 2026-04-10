ValueError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/dashboard-proveedores/streamlit_app.py", line 25, in <module>
    df["precio inicial"] = limpiar_numero(df["precio inicial"])
                           ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
File "/mount/src/dashboard-proveedores/streamlit_app.py", line 22, in limpiar_numero
    .astype(float)
     ~~~~~~^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/generic.py", line 6541, in astype
    new_data = self._mgr.astype(dtype=dtype, errors=errors)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/internals/managers.py", line 611, in astype
    return self.apply("astype", dtype=dtype, errors=errors)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/internals/managers.py", line 442, in apply
    applied = getattr(b, f)(**kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/internals/blocks.py", line 607, in astype
    new_values = astype_array_safe(values, dtype, errors=errors)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/dtypes/astype.py", line 240, in astype_array_safe
    new_values = astype_array(values, dtype, copy=copy)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/dtypes/astype.py", line 182, in astype_array
    values = values.astype(dtype, copy=copy)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/arrays/string_arrow.py", line 334, in astype
    return self.to_numpy(dtype=dtype, na_value=np.nan)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/arrays/arrow/array.py", line 1730, in to_numpy
    result[~mask] = data[~mask]._pa_array.to_numpy()
    ~~~~~~^^^^^^^
