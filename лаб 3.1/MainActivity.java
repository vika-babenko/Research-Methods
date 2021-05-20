package com.example.mndlab1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void click(View view) {

        EditText edNumber = findViewById(R.id.input);
        TextView tw = findViewById(R.id.textView);
        int number = Integer.parseInt(edNumber.getText().toString());
        if (number % 2 == 0) {
           tw.setText(number/2+"*2");
        }
        else {
        int x = (int) Math.ceil(Math.sqrt(number));
        
        while (!(Math.pow((int) Math.sqrt(x * x - number), 2) == x * x - number)) {
            x += 1;
        }
        int y = (int) Math.sqrt(x * x - number);
        tw.setText((x-y)+"*"+(x+y));
    }}

}