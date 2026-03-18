package com.example.myapplication;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    Button btncalcIMC;
    EditText dbpeso;
    EditText dbaltura;
    TextView IMC;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        dbpeso = (EditText) findViewById(R.id.txtpeso);
        dbaltura = (EditText) findViewById(R.id.txtaltura);
        IMC = (TextView) findViewById(R.id.lblIMC);
        result = (TextView) findViewById(R.id.txtresult);
        btncalcIMC = (Button) findViewById(R.id.btnIMC);
        btncalcIMC.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String imcnovo;
                double peso = Integer.parseInt(dbpeso.getText().toString());
                double altura = Integer.parseInt(dbaltura.getText().toString());
                double altura2 = altura / 100;
                double calc = peso / ((altura2 * altura2));
                if ((calc > 0) && calc <= 18.5)
                {
                    imcnovo = "Baixo peso";
                }
                else if ((calc > 18.6) && calc <= 24.9)
                {
                    imcnovo = "Peso normal";
                }
                else if ((calc > 25) && calc <= 29.9)
                {
                    imcnovo = "Excesso de peso";
                }
                else if ((calc > 30) && calc <= 34.9)
                {
                    imcnovo = "Obesidade";
                }
                else
                {
                    imcnovo = "Obesidade Extrema";
                }
                result.setText(String.valueOf(calc));
                IMC.setText(imcnovo);
            }
        });
    }
}