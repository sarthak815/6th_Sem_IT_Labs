package com.example.textencryption;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn = findViewById(R.id.encrypt_btn);
        EditText et = findViewById(R.id.input_tv);
        TextView tv = findViewById(R.id.output_tv);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String plain_text = String.valueOf(et.getText());
                String shift_key_txt = "2";
                int shift_key = Integer.parseInt(shift_key_txt);
                String cipher_text = "";
                for (int i = 0; i < plain_text.length(); i++) {
                    if(('Z' >= plain_text.charAt(i) && plain_text.charAt(i)>='A') || ('z' >= plain_text.charAt(i) && plain_text.charAt(i)>='a')){
                        char t = (char)((int)plain_text.charAt(i)+shift_key);
                        cipher_text += t;
                    }
                    else{
                        cipher_text += plain_text.charAt(i);
                    }
                }
                tv.setText(cipher_text);
            }
        });


    }
}