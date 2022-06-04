def skip(predicate, cell=None):
    '''Skips execution of the current cell if predicate evaluates to True.'''
    if eval(predicate):
        return

    get_ipython().ex(cell)


def load_ipython_extension(shell):
    '''Registers the skip magic when the extension loads.'''
    shell.register_magic_function(skip, 'line_cell')


def unload_ipython_extension(shell):
    '''Unregisters the skip magic when the extension unloads.'''
    del shell.magics_manager.magics['cell']['skip']
