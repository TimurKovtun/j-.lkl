import colorama
import inspect

intro_list = []
for method in dir(colorama):
    print(method)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))

print("модуль AnsiToWin32")
print(inspect.getmodule(colorama.AnsiToWin32))
print(callable(colorama.AnsiToWin32))
sig=inspect.signature(colorama.AnsiToWin32)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)


print("модуль colorama_text")
print(inspect.getmodule(colorama.colorama_text))
print(callable(colorama.colorama_text))
sig=inspect.signature(colorama.colorama_text)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)


print("модуль deinit")
print(inspect.getmodule(colorama.deinit))
print(callable(colorama.deinit))
sig=inspect.signature(colorama.deinit)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)


print("модуль init")
print(inspect.getmodule(colorama.init))
print(callable(colorama.init))
sig=inspect.signature(colorama.init)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)


print("модуль just_fix_windows_console")
print(inspect.getmodule(colorama.just_fix_windows_console))
print(callable(colorama.just_fix_windows_console))
sig=inspect.signature(colorama.just_fix_windows_console)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)

print("модуль reinit")
print(inspect.getmodule(colorama.reinit))
print(callable(colorama.reinit))
sig=inspect.signature(colorama.reinit)
for parametr in sig.parameters.values():
    print(parametr.name, parametr.default)