package mysqlswing;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.table.DefaultTableModel;

/**
 * CRUD Swing + DAO Corregido
 */
public class CrudProductosSwingTodoEnUno extends JFrame {

    // =========================
    // CONFIGURACIÓN DB
    // =========================
    private static final String DB_NAME = "empresa1";
    private static final String TABLE = "productos";
    private static final String URL = "jdbc:mysql://localhost:3306/" + DB_NAME
            + "?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";
    private static final String USER = "root";
    private static final String PASS = ""; 

    // =========================
    // UI
    // =========================
    private final JTextField txtId = new JTextField();  
    private final JTextField txtNombre = new JTextField();
    private final JTextField txtPrecio = new JTextField();
  
    private final DefaultTableModel modelo = new DefaultTableModel(
            new Object[] { "ID", "NOMBRE", "PRECIO" }, 0
    ) {
        @Override public boolean isCellEditable(int row, int col) { return false; }
    };

    private final JTable tabla = new JTable(modelo);
    private final JButton btnInsertar   = new JButton("Insertar");
    private final JButton btnActualizar = new JButton("Actualizar");
    private final JButton btnEliminar   = new JButton("Eliminar");
    private final JButton btnBuscar     = new JButton("Buscar (ID)");
    private final JButton btnListar     = new JButton("Listar");
    private final JButton btnLimpiar    = new JButton("Limpiar");

    public static void main(String[] args) {
        try { UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName()); } 
        catch (Exception ignored) {}
        SwingUtilities.invokeLater(CrudProductosSwingTodoEnUno::new);
    }

    public CrudProductosSwingTodoEnUno() {
        setTitle("CRUD Productos - " + DB_NAME);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(860, 520);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        txtId.setEditable(true);
        txtId.setBackground(Color.WHITE);

        add(crearPanelFormulario(), BorderLayout.NORTH);
        add(crearPanelTabla(), BorderLayout.CENTER);
        add(crearPanelBotones(), BorderLayout.SOUTH);

        configurarEventos();
        cargarTabla();

        setVisible(true);
    }

    private JPanel crearPanelFormulario() {
        JPanel p = new JPanel(new GridLayout(2, 3, 10, 10));
        p.setBorder(new TitledBorder("Datos del producto"));

        p.add(new JLabel("ID:"));
        p.add(new JLabel("NOMBRE:"));
        p.add(new JLabel("PRECIO:"));

        p.add(txtId);
        p.add(txtNombre);
        p.add(txtPrecio);

        return p;
    }

    private JScrollPane crearPanelTabla() {
        tabla.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        return new JScrollPane(tabla);
    }

    private JPanel crearPanelBotones() {
        JPanel p = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 10));
        p.add(btnInsertar);
        p.add(btnActualizar);
        p.add(btnEliminar);
        p.add(btnBuscar);
        p.add(btnListar);
        p.add(btnLimpiar);
        return p;
    }

    private void configurarEventos() {
        // Seleccionar fila
        tabla.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting() && tabla.getSelectedRow() != -1) {
                int fila = tabla.getSelectedRow();
                txtId.setText(String.valueOf(modelo.getValueAt(fila, 0)));
                txtNombre.setText(String.valueOf(modelo.getValueAt(fila, 1)));
                Object precio = modelo.getValueAt(fila, 2);
                txtPrecio.setText(precio == null ? "" : String.valueOf(precio));
            }
        });

        // Insertar
        btnInsertar.addActionListener(e -> {
            if (!validarCampos()) return;
            try {
                int id = Integer.parseInt(txtId.getText().trim());
                String nombre = txtNombre.getText().trim();
                String precio = txtPrecio.getText().trim();
                if (precio.isEmpty()) precio = null;

                if (insertar(id, nombre, precio)) {
                    JOptionPane.showMessageDialog(this, "Insertado correctamente.");
                    cargarTabla();
                    limpiar();
                }
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "ID o Precio inválidos.");
            }
        });

        // Actualizar
        btnActualizar.addActionListener(e -> {
            if (!validarCampos()) return;
            int id = Integer.parseInt(txtId.getText().trim());
            String nombre = txtNombre.getText().trim();
            String precio = txtPrecio.getText().trim();
            if (precio.isEmpty()) precio = null;

            if (actualizar(id, nombre, precio)) {
                JOptionPane.showMessageDialog(this, "Actualizado correctamente.");
                cargarTabla();
                limpiar();
            }
        });

        // Eliminar
        btnEliminar.addActionListener(e -> {
            String idTxt = txtId.getText().trim();
            if (idTxt.isEmpty()) return;
            int id = Integer.parseInt(idTxt);

            int confirm = JOptionPane.showConfirmDialog(this, "¿Eliminar ID " + id + "?", "Confirmar", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION && eliminar(id)) {
                JOptionPane.showMessageDialog(this, "Eliminado.");
                cargarTabla();
                limpiar();
            }
        });

        btnBuscar.addActionListener(e -> {
            String idTxt = JOptionPane.showInputDialog(this, "ID a buscar:");
            if (idTxt != null && !idTxt.trim().isEmpty()) {
                String[] fila = buscarPorId(Integer.parseInt(idTxt.trim()));
                if (fila != null) {
                    txtId.setText(fila[0]);
                    txtNombre.setText(fila[1]);
                    txtPrecio.setText(fila[2]);
                } else {
                    JOptionPane.showMessageDialog(this, "No encontrado.");
                }
            }
        });

        btnListar.addActionListener(e -> cargarTabla());
        btnLimpiar.addActionListener(e -> limpiar());
    }

    private boolean validarCampos() {
        if (txtId.getText().trim().isEmpty() || txtNombre.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "ID y Nombre son obligatorios.");
            return false;
        }
        return true;
    }

    private void cargarTabla() {
        modelo.setRowCount(0);
        for (String[] fila : listarTodos()) {
            modelo.addRow(fila);
        }
    }

    private void limpiar() {
        txtId.setText("");
        txtNombre.setText("");
        txtPrecio.setText("");
        tabla.clearSelection();
    }

    private static Connection getConexion() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASS);
    }

    // =========================
    // DAO (CORREGIDO)
    // =========================
    
    private boolean insertar(int id, String nombre, String precio) {
        String sql = "INSERT INTO " + TABLE + " (id, nombre, precio) VALUES (?, ?, ?)";
        try (Connection cn = getConexion();
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setInt(1, id);
            ps.setString(2, nombre);
            // Manejo correcto de nulos para el precio
            if (precio == null) ps.setNull(3, Types.VARCHAR); 
            else ps.setString(3, precio);

            return ps.executeUpdate() == 1;
        } catch (SQLException e) {
            mostrarErrorSQL("INSERTAR", e);
            return false;
        }
    }

    private boolean actualizar(int id, String nombre, String precio) {
        String sql = "UPDATE " + TABLE + " SET nombre=?, precio=? WHERE id=?";
        try (Connection cn = getConexion();
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setString(1, nombre);
            if (precio == null) ps.setNull(2, Types.VARCHAR);
            else ps.setString(2, precio);
            ps.setInt(3, id);

            return ps.executeUpdate() == 1;
        } catch (SQLException e) {
            mostrarErrorSQL("ACTUALIZAR", e);
            return false;
        }
    }

    private boolean eliminar(int id) {
        String sql = "DELETE FROM " + TABLE + " WHERE id=?";
        try (Connection cn = getConexion();
             PreparedStatement ps = cn.prepareStatement(sql)) {
            ps.setInt(1, id);
            return ps.executeUpdate() == 1;
        } catch (SQLException e) {
            mostrarErrorSQL("ELIMINAR", e);
            return false;
        }
    }

    private String[] buscarPorId(int id) {
        String sql = "SELECT id, nombre, precio FROM " + TABLE + " WHERE id=?";
        try (Connection cn = getConexion();
             PreparedStatement ps = cn.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return new String[] { String.valueOf(rs.getInt("id")), rs.getString("nombre"), rs.getString("precio") };
                }
            }
        } catch (SQLException e) { mostrarErrorSQL("BUSCAR", e); }
        return null;
    }

    private List<String[]> listarTodos() {
        String sql = "SELECT id, nombre, precio FROM " + TABLE + " ORDER BY id";
        List<String[]> lista = new ArrayList<>();
        try (Connection cn = getConexion();
             Statement st = cn.createStatement();
             ResultSet rs = st.executeQuery(sql)) {
            while (rs.next()) {
                lista.add(new String[] { String.valueOf(rs.getInt("id")), rs.getString("nombre"), rs.getString("precio") });
            }
        } catch (SQLException e) { mostrarErrorSQL("LISTAR", e); }
        return lista;
    }

    private void mostrarErrorSQL(String operacion, SQLException e) {
        JOptionPane.showMessageDialog(this, "Error en " + operacion + ": " + e.getMessage(), "Error SQL", JOptionPane.ERROR_MESSAGE);
    }
}