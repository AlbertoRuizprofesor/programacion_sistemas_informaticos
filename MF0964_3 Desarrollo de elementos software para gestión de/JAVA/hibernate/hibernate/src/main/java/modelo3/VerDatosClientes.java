package modelo3;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.context.internal.ThreadLocalSessionContext;
import org.hibernate.engine.spi.SessionFactoryImplementor;
import org.hibernate.query.Query;

import java.util.List;

public class VerDatosClientes {

    public static void main(String[] args) {

        // Configurar la sesión de Hibernate
        SessionFactory sessionFactory = new Configuration()
                .configure()
                .buildSessionFactory();
        /*LAS SESIONES FUNCIONA COMO CACHE, PERMITE ACCEDER A LA BASE DE DATOS UNA VEZ EN LA SESIÓN
        ACCEDER VARIAS VECES MAS RAPIDEZ, LO QUE HACE QUE EL ACCESO SEA MAS RAPIDO, LOS CAMBIOS EN LA
        SESIÓN SE REALIZAN MAS RAPIDOS, SE USA UN LENGUAJE QUE EN VEZ DE SQL ES HQL
         */

        // Configurar la sesión en el contexto actual
        ThreadLocalSessionContext context = new ThreadLocalSessionContext((SessionFactoryImplementor) 
        		sessionFactory);
        context.bind(sessionFactory.openSession());

        try {
            // Obtener la sesión actual
            Session session = context.currentSession();

            // Iniciar transacción
            session.beginTransaction();

            // Crear consulta HQL para seleccionar todos los registros de la tabla fabricante
            String hql = "FROM Clientes";
            Query<Clientes> query = session.createQuery(hql, Clientes.class);

            // Ejecutar consulta y obtener resultados
            List<Clientes> clientes = query.list();

            // Imprimir resultados
            System.out.println("Registros en la tabla clientes:");
            for (Clientes f : clientes) {
                System.out.println(f.toString());
            }

            session.getTransaction().commit(); //LOS CAMBIOS SE GUARDAN, SI SE PUSIERA ROLLBACK NO SE GUARDARIAN

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            context.unbind(sessionFactory);
            sessionFactory.close();  //CERRAMOS LA SESIÓN
        }
    }
}
