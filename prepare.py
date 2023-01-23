import json
import os
import jsonpickle


def prepare_prompt_completion(listing):
    prompt = f"{listing.full_address}. It is a {listing.property_type}. It has {listing.bedrooms} bedrooms. It has {listing.bathrooms} bathrooms. It has {listing.parking_spaces} parking spaces. It is on a {listing.land_size} block. It's {listing.price}. \n\n###\n\n"
    completion = listing.description

    line = {"prompt": prompt, "completion": f" {completion} END"}
    return line


def prepare_prompt_completions():
    lines = []
    for filename in os.listdir("data"):
        with open("data/" + filename, "r") as f:
            listing = jsonpickle.decode(f.read())
            lines.append(prepare_prompt_completion(listing))
    with open("gpt_3_train.jsonl", "w") as f:
        for l in lines:
            f.write(f"{json.dumps(l)}\n")


if __name__ == "__main__":
    prepare_prompt_completions()
