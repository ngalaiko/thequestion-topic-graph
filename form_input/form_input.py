from slugify import slugify

def read_topics():
    topics = []
    ids = []
    with open('./topics.txt') as f:
        for l in f:     
            ids.append(int(l.split('|')[0].strip()))
            topics.append(l.split('|'))
    return topics, ids
                    
def read_topic_ids():
          topic_ids = []
          with open('./topic_ids.txt') as f:
              for l in f:       
                  topic_ids.append(l.replace('{', '').replace('}', '').split(','))
          return topic_ids
                    
def make_graph_dict(topic_ids, idd):
      graph = {}
      for ids in topic_ids:
          for i, t1 in enumerate(ids):
              if int(t1.strip()) in idd:
                  for t2 in ids[i + 1:]:
                      if int(t2.strip()) in idd:
                          try:
                              graph[(t1, t2)] +=  1
                          except:
                              graph[(t1, t2)] =  1
      return graph
                            
topics, ids = read_topics()
topic_ids = read_topic_ids()
graph = make_graph_dict(topic_ids, ids)

# deleting thin edges
for k, v in graph.items():
    if v < 7:
        graph.pop(k, None)

with open('../input.in', 'w') as f:
    f.write(str(len(topics)) + ' ' + str(len(graph)) + '\n')
    vv = 0
    ee = 0 
    for t in topics:
	ee += 1
	f.write(t[0].strip() + ' ' + slugify(t[-1].strip()) + '\n')
    for k, v in graph.items():
	vv += 1
        f.write(k[0].strip() + ' ' + k[1].strip() + ' ' + str(v) + '\n')
print(ee, vv)
