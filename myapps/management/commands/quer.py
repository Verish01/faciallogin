from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_path = 'gaussalgo/T5-LM-Large-text2sql-spider'
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# question = "give the lowest cost per item from myapp_inventory database"
question = "give the lowest temperature from myapps_weather database"
schema = '''"myapps_weather" "DATABASE" 
                        "id" int, 
                        "formatted_date" datetime, 
                        "summary" varchar(200), 
                        "precip_type" varchar(50), 
                        "temperature_c" float, 
                        "apparent_temperature_c" float, 
                        "humidity" float, 
                        "wind_speed_kmh" float, 
                        "wind_bearing_degrees" int, 
                        "visibility_km" float, 
                        "cloud_cover" float, 
                        "pressure_millibars" float, 
                        "daily_summary" text, 
                        primary key: "id"'''
# schema =""""myapps_inventory" "DATABASE" 
#     "product_ID" int, 
#     "product_name" text, 
#     "quantity_in_stock" int, 
#     "cost_per_item" float, 
#     primary key: "product_ID"""""


input_text = " ".join(["Question: ",question, "Schema:", schema])

model_inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**model_inputs, max_length=512)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

print("SQL Query:")
print(output_text)
