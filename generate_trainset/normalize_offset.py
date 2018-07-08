def normalize_offsets(offsets: list) -> list:
    """
    Normalize the provided list of offsets by merging or removing some of them
    :param offsets: original offsets as list of tuples generated by pattern matching
    :return: cleaned list of tuples
    """
    sorted_offsets = sorted(offsets, key=lambda tup: tup[0])
    offset_to_keep = list()
    previous_start_offset, previous_end_offset, previous_type_tag = None, None, None

    for current_start_offset, current_end_offset, current_type_tag in sorted_offsets:

        # merge tags which appear as separated but are not really
        if (previous_end_offset is not None) and (previous_end_offset + 2 == current_start_offset):
            previous_start_offset, previous_end_offset, previous_type_tag = previous_start_offset, \
                                                                            current_end_offset, \
                                                                            current_type_tag

        if (previous_end_offset is not None) and (previous_end_offset < current_end_offset):
            offset_to_keep.append((previous_start_offset, previous_end_offset, previous_type_tag))

        # keep longest tags when they are one on the other
        if (previous_end_offset is not None) and (previous_end_offset >= current_end_offset):
            current_start_offset, current_end_offset, current_type_tag = previous_start_offset, \
                                                                         previous_end_offset, \
                                                                         previous_type_tag

        previous_start_offset, previous_end_offset, previous_type_tag = current_start_offset, \
                                                                        current_end_offset, \
                                                                        current_type_tag

    offset_to_keep.append((previous_start_offset, previous_end_offset, previous_type_tag))
    return offset_to_keep


