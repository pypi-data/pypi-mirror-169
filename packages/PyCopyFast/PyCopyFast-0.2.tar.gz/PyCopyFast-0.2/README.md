PytonWrapper for [GitHub - FastCopyLab/FastCopy](https://github.com/FastCopyLab/FastCopy)

Very easy to use:

```python
pip install PyCopyFast
```

```python
        pathfastcopy = r"C:\path\fcp.exe"
        path1 = "c:\\blabla"
        path2 = "c:\\blabla2"
        asz = (
            FastCopy(pathfastcopy)
            .force_close()
            .no_confirm_del()
            .force_start()
            .error_stop("=FALSE", join_value=True)
            .speed("full")
            .log("=FALSE", join_value=True)
            # .srcf
            .to(path2)
            .cmd_diff(path1)
            .r_subprocess_run()
        )
        for xx in asz.stdout.decode("utf-8", "ignore").splitlines():
            print(xx)
```

## Make sure to call the cmd functions

### (cmd_noexist_only, cmd_diff, cmd_update, cmd_force_copy, cmd_sync, cmd_move, cmd_delete) right before the XXXXrun() function

### Otherwise, it might now work.
