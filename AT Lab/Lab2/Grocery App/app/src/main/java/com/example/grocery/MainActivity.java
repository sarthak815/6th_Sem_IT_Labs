package com.example.grocery;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ListView listView ;

// Get ListView object from xml
            listView = (ListView) findViewById(R.id.grocery_it);

// Defined Array values to show in ListView
            String[] values = new String[] { "Bananas",
                    "Eggs",
                    "Milk",
                    "Chocolate",
                    "Tomatoes",
                    "Potatoes",
                    "Onion",
                    "Yoghurt"
            };
            // First parameter - Context
// Second parameter - Layout for the row
// Third parameter - ID of the TextView to which the data is written
// Forth - the Array of data
            ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                    android.R.layout.simple_list_item_1, android.R.id.text1, values);

// Assign adapter to ListView
            listView.setAdapter(adapter);

// ListView Item Click Listener
            listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> parent, View view,
                                        int position, long id) {

// ListView Clicked item index
                    int itemPosition = position;
// ListView Clicked item value
                    String itemValue = (String) listView.getItemAtPosition(position);

// Show Alert
                    Toast.makeText(getApplicationContext(),
                            "Position :"+itemPosition+" ListItem : " +itemValue ,
                            Toast.LENGTH_SHORT)
                            .show();
                }
            });
        }
    }

