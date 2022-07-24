import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name = 'run2', checkpoint_dir='checkpoint')
text = gpt2.generate(
    sess,
    run_name = 'run2',
    checkpoint_dir='checkpoint',
    length=250,
    temperature=.6,
    #destination_path='bottext',
    prefix=None,
    return_as_list=True
)
print(text)
