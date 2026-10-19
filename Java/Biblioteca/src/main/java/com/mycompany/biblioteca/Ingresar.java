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

        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
}
