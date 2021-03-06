#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.
from typing import List, Tuple

from spacy import displacy
from spacy.tokens.doc import Doc

from ner.model_factory import get_empty_model, colors
from xml_extractions.extract_node_values import Offset


def convert_offsets_to_spacy_docs(doc_annotated: List[Tuple[str, str, List[Offset]]]) -> List[Doc]:
    """
    Convert a list of tuple of string with their offset to Spacy doc with entities ready
    :param doc_annotated: list of tuple (string, array of offsets)
    :return: list of spacy doc
    """
    model = get_empty_model(load_labels_for_training=False)
    docs: List[Doc] = list()

    for (index, (case_id, text, tags)) in enumerate(doc_annotated):
        doc: Doc = model.make_doc(text)
        ents = list()
        for offset in tags:
            span_doc = doc.char_span(offset.start, offset.end, label=offset.type)
            if span_doc is not None:
                ents.append(span_doc)
            else:
                print("Issue in offset", "Index: " + str(index), "case: " + case_id,
                      text[offset.start:offset.end], text, sep="|")
        doc.ents = ents
        docs.append(doc)
    return docs
