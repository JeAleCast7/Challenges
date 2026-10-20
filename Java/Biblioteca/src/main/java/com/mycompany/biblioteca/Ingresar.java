package com.mycompany.biblioteca;
import java.sql.*;

public class Ingresar {
    public boolean validar(String correo, String pwd){
        String consulta = "SELECT 1 FROM usuarios WHERE correo = ? AND pwd = ?";

        try (Connection con = Conexion.getConexion();
             PreparedStatement ps = con.prepareStatement(consulta)) {

            ps.setString(1, correo);
            ps.setString(2, pwd);

            try (ResultSet rs = ps.executeQuery()) {
                return rs.next();
            }

        }   catch (SQLException e) {
                e.printStackTrace();
                return false;
        }
    }
    
    public boolean registrar(int cedula, String nombre, String correo, String pwd){
        String insertar = "INSERT INTO usuarios (cedula, nombre, correo, pwd) VALUES (?, ?, ?, ?)";
        
        try (Connection con = Conexion.getConexion();
             PreparedStatement ps = con.prepareStatement(insertar)) {
                 
            ps.setInt   (1, cedula);
            ps.setString(2, nombre);
            ps.setString(3, correo);
            ps.setString(4, pwd);
            
            return ps.executeUpdate() > 0;            
             
        }   catch (SQLException e){
                e.printStackTrace();
                return false;
            } 
    }
}

