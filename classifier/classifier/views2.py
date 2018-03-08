from django.http import HttpResponse
import sys
import tensorflow as tf








def info(response):
    image_path = '/home/shorav/virtual/classifier/classifier/test.jpg'
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("final_labels.txt")]

# Unpersists graph from file
    with tf.gfile.FastGFile("./final_graph.pb",'rb') as f:
        graph_def = tf.GraphDef()

        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first gggfgfprediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    score_results=[]
    final_label=[]
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
        score_results.append(score)
        final_label.append(human_string)

    a= max(score_results)
    c=score_results.index(a)
    return HttpResponse(final_label[c])


#print "This is my final output ", final_label[c]    
	










