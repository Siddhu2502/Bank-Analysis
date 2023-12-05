
import com.mongodb.{ServerApi, ServerApiVersion}
import org.mongodb.scala.{ConnectionString, MongoClient, MongoClientSettings}
import org.mongodb.scala.bson.Document

import scala.concurrent.Await
import scala.concurrent.duration.DurationInt
import scala.util.Using

object MongoClientConnectionExample {

  def main(args: Array[String]): Unit = {

    val connectionString = "mongodb+srv://siddhu2502:best1234@bigdataproj.ooixpnk.mongodb.net/?retryWrites=true&w=majority";

    // Construct a ServerApi instance using the ServerApi.builder() method
    val serverApi = ServerApi.builder.version(ServerApiVersion.V1).build()

    val settings = MongoClientSettings
      .builder()
      .applyConnectionString(ConnectionString(connectionString))
      .serverApi(serverApi)
      .build()

    // Create a new client and connect to the server
    Using(MongoClient(settings)) { mongoClient =>
      // Send a ping to confirm a successful connection
      val database = mongoClient.getDatabase("bigdataproj")
      val ping = database.runCommand(Document("ping" -> 1)).head()

      Await.result(ping, 10.seconds)
      System.out.println("Pinged your deployment. You successfully connected to MongoDB!")
    }

  }
}