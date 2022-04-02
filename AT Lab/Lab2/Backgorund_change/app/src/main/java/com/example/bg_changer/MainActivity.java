package com.example.bg_changer;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        LinearLayout linearLayout = findViewById(R.id.lin_layout);
        Button btnb,btng;
        btnb = findViewById(R.id.blue_btn);
        btng = findViewById(R.id.green_btn);
        btnb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                linearLayout.setBackgroundColor(Color.parseColor("#0000FF"));

            }
        });
        btng.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                linearLayout.setBackgroundColor(Color.parseColor("#00FF00"));
            }
        });
    }
}