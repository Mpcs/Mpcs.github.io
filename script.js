var names_pl;
var names_en;

fetch('./translation_names_EN.json')
  .then(response => response.json())
  .then(data => names_en = data)
  .then()
  .catch(error => console.log(error));

fetch('./translation_names_PL.json')
  .then(response => response.json())
  .then(data => names_pl = data)
  .then()
  .catch(error => console.log(error));


function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

function search_input() {
    var out_element = document.getElementById("output")
    var input_element = document.getElementById("input")
    
    let regex = new RegExp(input_element.value, 'i');

    var categories = Object.keys(names_en)
    var total_matched_keys = categories.slice()

    categories.forEach(category => {
        var english_entries = Object.entries(names_en[category]);
        var polish_entries = Object.entries(names_pl[category]);

        var filtered_entries_en = english_entries.filter(([key, value]) => (key.match(regex) || value.match(regex)) );
        var filtered_entries_pl = polish_entries.filter(([key, value]) => (key.match(regex) || value.match(regex)) );

        var converted_entries_en = Object.fromEntries(filtered_entries_en);
        var converted_entries_pl = Object.fromEntries(filtered_entries_pl);
        
        total_matched_keys[category] = (Object.keys(converted_entries_en).slice().concat(Object.keys(converted_entries_pl))).filter(onlyUnique);
    })

    console.log(total_matched_keys)

    out_element.innerHTML = '';

    var sum = 0;
    total_matched_keys.forEach(category => {
        
        total_matched_keys[category].forEach(key => {
            if(sum < 100) {
                let li = document.createElement('div');
                out_element.appendChild(li);
        
                var pl_name = names_pl[category][key];
                var en_name = names_en[category][key];
                
                li.innerHTML = "<h6>" + key + "</h6>" + "<p>PL - " + pl_name + "</p>" + "<p>EN - " + en_name + "</p>";

                //li.innerHTML += "CATEGORY: " + category +" <b>ID:</b> " + key + " <b>PL</b>: " + pl_name + " <b>EN</b>: " + en_name;
                sum += 1;
            }
        })
    })
}
