
import os
import importlib

def get_all_models():
    return ['clser', 'deepinversion', 'der', 'derpp', 'dgr', 'discoil', 'gem', 'gpm', 'gss', 'hal', 'joint', 'lwf', 'lwm', 'oewc', 'pass', 'pnn', 'si']

names = {}
for model in get_all_models():
    mod = importlib.import_module('deepinc.models.' + model)
    class_name = {x.lower():x for x in mod.__dir__()}[model.replace('_', '')]
    names[model] = getattr(mod, class_name)

def get_model(args, backbone, loss, transform):
    return names[args.model](backbone, loss, args, transform)

def get_il_model(args):
    return names[args.model](args)
