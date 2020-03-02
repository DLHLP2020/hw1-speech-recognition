import sys
import numpy as np
import pandas as pd
import editdistance as ed

SEP = ' '

def cal_cer(row):
    return 100*float(ed.eval(row.hyp, row.truth))/len(row.truth)


def cal_wer(row):
    return 100*float(ed.eval(row.hyp.split(SEP), row.truth.split(SEP)))/len(row.truth.split(SEP))

# Evaluation
predict = pd.read_csv(sys.argv[1], sep=',')
result = pd.read_csv(sys.argv[2], sep=',')
result['id'] = predict['answer']
result.columns = ['hyp', 'truth']
result['hyp_char_cnt'] = result.apply(lambda x: len(x.hyp), axis=1)
result['hyp_word_cnt'] = result.apply(lambda x: len(x.hyp.split(SEP)), axis=1)
result['truth_char_cnt'] = result.apply(lambda x: len(x.truth), axis=1)
result['truth_word_cnt'] = result.apply(
    lambda x: len(x.truth.split(SEP)), axis=1)
result['cer'] = result.apply(cal_cer, axis=1)
result['wer'] = result.apply(cal_wer, axis=1)

# Show results
print()
print('============  Result of', sys.argv[2], '============')
print(' -----------------------------------------------------------------------')
print('| Statics\t\t|  Truth\t|  Prediction\t| Abs. Diff.\t|')
print(' -----------------------------------------------------------------------')
print('| Avg. # of chars\t|  {:.2f}\t|  {:.2f}\t|  {:.2f}\t\t|'.
      format(result.truth_char_cnt.mean(), result.hyp_char_cnt.mean(),
             np.mean(np.abs(result.truth_char_cnt-result.hyp_char_cnt))))
print('| Avg. # of words\t|  {:.2f}\t|  {:.2f}\t|  {:.2f}\t\t|'.
      format(result.truth_word_cnt.mean(), result.hyp_word_cnt.mean(),
             np.mean(np.abs(result.truth_word_cnt-result.hyp_word_cnt))))
print(' -----------------------------------------------------------------------')
print(' ---------------------------------------------------------------')
print('| Error Rate (%)| Mean\t\t| Std.\t\t| Min./Max.\t|')
print(' ---------------------------------------------------------------')
print('| Character\t| {:2.4f}\t| {:.2f}\t\t| {:.2f}/{:.2f}\t|'.format(result.cer.mean(), result.cer.std(),
                                                                      result.cer.min(), result.cer.max()))
print('| Word\t\t| {:2.4f}\t| {:.2f}\t\t| {:.2f}/{:.2f}\t|'.format(result.wer.mean(), result.wer.std(),
                                                                   result.wer.min(), result.wer.max()))
print(' ---------------------------------------------------------------')
print('Note : If the text unit is phoneme, WER = PER and CER is meaningless.')
print()
