package com.example.myapplication3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText et_phone = findViewById(R.id.phone_tv);
        EditText et_email = findViewById(R.id.email_tv);
        String email = et_email.getText().toString();
        String phone = et_phone.getText().toString();
        Button submit = findViewById(R.id.submit);
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(phone.length()==10){

                }
                if(email.lastIndexOf("@")<email.lastIndexOf(".")){

                }
                else{
                    Toast.makeText(getApplicationContext(), "Phone Number or email invalid", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }


}