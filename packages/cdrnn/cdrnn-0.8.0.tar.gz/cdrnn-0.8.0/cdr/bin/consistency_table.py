import sys
import re
import os
import numpy as np
import argparse
from cdr.config import Config
from cdr.util import sn

matcher = re.compile('(_(main|rep\d))')

def new_row(system, results):
    s = system
    out = s
    tasks = list(results.keys())
    for t in tasks:
        if t in results and s in results[t]:
            if 'train' in results[t][s]:
                train = ''
                arr = np.array(results[t][s]['train'])
                _med = np.median(arr)
                _min = arr.min()
                _max = arr.max()
                _spread = _max - _min
                _med = '%.4f' % _med
                _min = '%.4f' % _min
                _max = '%.4f' % _max
                _spread = '%.4f' % _spread
                if len(_med.split('.')[0]) > 3:
                    _med = '%d' % round(float(_med))
                train += _med
                if len(_min.split('.')[0]) > 3:
                    _min = '%d' % round(float(_min))
                train += ' & %s' % _min
                if len(_max.split('.')[0]) > 3:
                    _max = '%d' % round(float(_max))
                train += ' & %s' % _max
                if len(_spread.split('.')[0]) > 3:
                    _spread = '%d' % round(float(_spread))
                train += ' & %s' % _spread
            else:
                train = '--- & --- & --- & ---'
            if 'dev' in results[t][s]:
                dev = ''
                arr = np.array(results[t][s]['dev'])
                _med = np.median(arr)
                _min = arr.min()
                _max = arr.max()
                _spread = _max - _min
                _med = '%.4f' % _med
                _min = '%.4f' % _min
                _max = '%.4f' % _max
                _spread = '%.4f' % _spread
                if len(_med.split('.')[0]) > 3:
                    _med = '%d' % round(float(_med))
                dev += _med
                if len(_min.split('.')[0]) > 3:
                    _min = '%d' % round(float(_min))
                dev += ' & %s' % _min
                if len(_max.split('.')[0]) > 3:
                    _max = '%d' % round(float(_max))
                dev += ' & %s' % _max
                if len(_spread.split('.')[0]) > 3:
                    _spread = '%d' % round(float(_spread))
                dev += ' & %s' % _spread
            else:
                dev = '--- & --- & --- & ---'
            out += ' & ' + ' & '.join([train, dev])
        else:
            out += ' & ' + ' & '.join(['---'] * 3)
    out += '\\\\\n'
    return out
    

def results_to_table(results, systems, indent=4):
    tasks = results.keys()
    out = ''
    out += '\\begin{table}\n'
    out += ' ' * indent + '\\begin{tabular}{r|%s}\n' % ('|'.join(['cccc'] * 2 * len(tasks)))

    out += ' ' * (indent * 2) + ' & '.join(['Dataset'] + ['\\multicolumn{8}{|c}{%s}' % t for t in tasks]) + '\\\\\n'
    out += ' ' * (indent * 2) + ' & '.join([''] + ['\\multicolumn{4}{|c}{%s}' % p for t in tasks for p in ('train', 'dev')]) + '\\\\\n'
    out += ' ' * (indent * 2) + '& ' + ' & '.join(['Median', 'Min', 'Max', 'Spread'] * len(tasks) * 2) + '\\\\\n'
    out += ' ' * (indent * 2) + '\\hline\n'

    for s in systems:
        out += ' ' * (indent * 2) + new_row(s, results)
 
    out += ' ' * indent + '\\end{tabular}\n'
    out += '\\end{table}\n'

    return out


if __name__ == '__main__':
    argparser = argparse.ArgumentParser('''
    Generate a LaTeX table summarizing results from CDR vs. baseline models in some output directory.
    Tasks are defined as sets of experiments within the same config file (because they are constrained to use the same data).
    ''')
    argparser.add_argument('config_paths', nargs='+', help='Path(s) to config files defining models to compare.')
    argparser.add_argument('-m', '--metric', default='err', help='Metric to report. One of ``["err", "loglik", "iter"]``.')
    argparser.add_argument('-c', '--collapse_response', action='store_true', help='Collapse all responses into a single measure (for multivariate models).')
    args = argparser.parse_args()

    if args.metric.lower() in ['err', 'mse', 'loss']:
        metric = 'MSE'
    elif args.metric.lower() in ['loglik', 'll', 'likelihood']:
        metric = 'Loglik'
    elif args.metric.lower() in ['n', 'iter', 'niter', 'n_iter']:
        metric = 'Training iterations completed'
    else:
        raise ValueError('Unrecognized metric: %s.' % args.metric)
    collapse_response = args.collapse_response

    results = {}
    systems = []
    for i, path in enumerate(args.config_paths):
        p = Config(path)
        models = [x for x in p.model_list if matcher.search(x)]
        name = os.path.splitext(os.path.basename(path))[0]
        systems.append(name)
        for j, s in enumerate(models):
            if s in p.model_list:
                s_path = s.replace(':', ':')
                for partition in ['train', 'dev']:
                    if os.path.exists(p.outdir + '/' + s_path):
                        for path in os.listdir(p.outdir + '/' + s_path):
                            if path.startswith('eval') and path.endswith('%s.txt' % partition):
                                eval_path = p.outdir + '/' + s_path + '/' + path
                                _response = path.split('_')[1]
                                if collapse_response:
                                    _response = metric
                                if _response not in results:
                                    results[_response] = {}
                                if name not in results[_response]:
                                    results[_response][name] = {}
                                if partition not in results[_response][name]:
                                    results[_response][name][partition] = []
                                with open(eval_path, 'r') as f:
                                    line = f.readline()
                                    while line:
                                        if line.strip().startswith(metric):
                                            val = float(line.strip().split()[-1])
                                            results[_response][name][partition].append(val)
                                        line = f.readline()

    print(results_to_table(results, systems))


